#!/usr/bin/env python3
"""Bounded exact census for the first L1 mixed-petal growth-law point.

This is the roadmap N10 pilot, not the parked L1-ESQ campaign.  It enumerates
only floor-band supports that can be complete agreement sets at n=16 or 32,
interpolates one degree-<k polynomial, and retains the support only when the
complete agreement set is exactly the candidate.  The n=16 consecutive-scale
run must reproduce the banked count 43 before either n=32 result is accepted.

Resources: one CPU, 1 GiB, one container, 60 seconds.  The C++ worker prints
atomic progress checkpoints.  Timeout means INCOMPLETE and is not a PASS.
"""

from __future__ import annotations

import json
import subprocess
import tempfile
import time

import modal


APP_NAME = "l1-balanced-mixed-growth-census"

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").apt_install("g++")


CPP_SOURCE = r'''
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using i64 = std::int64_t;

static i64 mod_pow(i64 a, i64 e, i64 p) {
    i64 out = 1;
    while (e) {
        if (e & 1) out = out * a % p;
        a = a * a % p;
        e >>= 1;
    }
    return out;
}

static i64 inv(i64 a, i64 p) {
    a %= p;
    if (a < 0) a += p;
    return mod_pow(a, p - 2, p);
}

static std::vector<i64> domain(int p, int n) {
    for (int g = 2; g < p; ++g) {
        i64 z = mod_pow(g, (p - 1) / n, p);
        if (mod_pow(z, n, p) == 1 && mod_pow(z, n / 2, p) != 1) {
            std::vector<i64> out(n, 1);
            for (int j = 1; j < n; ++j) out[j] = out[j - 1] * z % p;
            return out;
        }
    }
    throw std::runtime_error("no domain generator");
}

static i64 eval(const std::vector<i64>& f, i64 x, i64 p) {
    i64 value = 0;
    for (auto it = f.rbegin(); it != f.rend(); ++it) {
        value = (value * x + *it) % p;
    }
    return value;
}

static std::vector<i64> interpolate(
    const std::vector<int>& points,
    const std::vector<i64>& xs,
    const std::vector<i64>& ys,
    i64 p
) {
    const int k = static_cast<int>(points.size());
    std::vector<i64> product(1, 1);
    for (int index : points) {
        std::vector<i64> next(product.size() + 1, 0);
        for (int j = 0; j < static_cast<int>(product.size()); ++j) {
            next[j] = (next[j] - product[j] * xs[index]) % p;
            next[j + 1] = (next[j + 1] + product[j]) % p;
        }
        product.swap(next);
    }

    std::vector<i64> answer(k, 0);
    for (int ii = 0; ii < k; ++ii) {
        const int index = points[ii];
        const i64 root = xs[index];
        std::vector<i64> quotient(k, 0);
        quotient[k - 1] = product[k];
        for (int j = k - 2; j >= 0; --j) {
            quotient[j] = (product[j + 1] + root * quotient[j + 1]) % p;
        }
        i64 denominator = eval(quotient, root, p);
        i64 scale = ys[index] * inv(denominator, p) % p;
        for (int j = 0; j < k; ++j) {
            answer[j] = (answer[j] + scale * quotient[j]) % p;
        }
    }
    for (i64& coefficient : answer) {
        coefficient %= p;
        if (coefficient < 0) coefficient += p;
    }
    return answer;
}

struct Layout {
    std::vector<int> core;
    std::vector<std::array<int, 2>> petals;
    int background;
};

static Layout layout(int n) {
    const int k = n / 2;
    const int half = n / 2;
    const int nf = (k - 1) / 2;
    Layout out;
    for (int j = 0; j < nf; ++j) {
        out.core.push_back(j);
        out.core.push_back(j + half);
    }
    out.core.push_back(nf);
    out.background = nf + half;
    for (int j = nf + 1; j < half; ++j) {
        out.petals.push_back({j, j + half});
    }
    return out;
}

static std::vector<i64> chart_word(
    int n,
    int p,
    const std::string& mode,
    const std::vector<i64>& xs,
    const Layout& shape
) {
    std::vector<i64> values(n, 0);
    i64 geometric = 1;
    for (int petal_index = 0;
         petal_index < static_cast<int>(shape.petals.size());
         ++petal_index) {
        i64 scalar = mode == "consec" ? petal_index + 1 : geometric;
        geometric = geometric * 5 % p;
        for (int point : shape.petals[petal_index]) {
            i64 value = scalar;
            for (int root : shape.core) {
                value = value * ((xs[point] - xs[root] + p) % p) % p;
            }
            values[point] = value;
        }
    }
    return values;
}

static void choose(
    const std::vector<int>& source,
    int count,
    int start,
    std::vector<int>& current,
    std::vector<std::vector<int>>& output
) {
    if (static_cast<int>(current.size()) == count) {
        output.push_back(current);
        return;
    }
    for (int j = start;
         j <= static_cast<int>(source.size()) -
                  (count - static_cast<int>(current.size()));
         ++j) {
        current.push_back(source[j]);
        choose(source, count, j + 1, current, output);
        current.pop_back();
    }
}

static std::vector<std::vector<int>> combinations(
    const std::vector<int>& source,
    int count
) {
    std::vector<std::vector<int>> output;
    std::vector<int> current;
    choose(source, count, 0, current, output);
    return output;
}

static bool mixed_omission(
    const std::vector<int>& omitted,
    const Layout& shape
) {
    for (const auto& petal : shape.petals) {
        int hits = 0;
        for (int point : omitted) {
            hits += point == petal[0] || point == petal[1];
        }
        if (hits == 1) return true;
    }
    return false;
}

static void print_checkpoint(
    int n,
    const std::string& mode,
    int shard_index,
    int shard_count,
    std::uint64_t processed,
    std::uint64_t retained,
    const std::chrono::steady_clock::time_point& began
) {
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - began
    ).count();
    std::cout << "L1_N10_CHECKPOINT {\"n\":" << n
              << ",\"mode\":\"" << mode
              << "\",\"shard_index\":" << shard_index
              << ",\"shard_count\":" << shard_count
              << ",\"processed\":" << processed
              << ",\"retained\":" << retained
              << ",\"seconds\":" << seconds << "}" << std::endl;
}

static std::uint64_t census(
    int n,
    int p,
    const std::string& mode,
    int shard_index = 0,
    int shard_count = 1
) {
    const int k = n / 2;
    const auto xs = domain(p, n);
    const auto shape = layout(n);
    const auto values = chart_word(n, p, mode, xs, shape);
    const int threshold = 2 * (static_cast<int>(shape.petals.size()) - 2);
    std::vector<int> petal_points;
    for (const auto& petal : shape.petals) {
        petal_points.push_back(petal[0]);
        petal_points.push_back(petal[1]);
    }

    const auto began = std::chrono::steady_clock::now();
    std::uint64_t candidates = 0;
    std::uint64_t processed = 0;
    std::uint64_t retained = 0;
    std::map<int, std::uint64_t> agreement_histogram;
    std::map<int, std::uint64_t> core_histogram;

    for (int core_count = 0; core_count <= 3; ++core_count) {
        if (static_cast<int>(shape.core.size()) - core_count < threshold) {
            continue;
        }
        const auto core_choices = combinations(shape.core, core_count);
        for (int use_background = 0; use_background <= 1; ++use_background) {
            for (int omitted_count = 1; omitted_count <= 3; ++omitted_count) {
                if (k + core_count + use_background - omitted_count < k + 1) {
                    continue;
                }
                const auto omission_choices = combinations(
                    petal_points, omitted_count
                );
                for (const auto& selected_core : core_choices) {
                    for (const auto& omitted : omission_choices) {
                        if (!mixed_omission(omitted, shape)) continue;
                        ++candidates;
                        if (static_cast<int>((candidates - 1) % shard_count) !=
                            shard_index) {
                            continue;
                        }
                        ++processed;
                        std::vector<char> support(n, 0);
                        for (int point : petal_points) support[point] = 1;
                        for (int point : omitted) support[point] = 0;
                        for (int point : selected_core) support[point] = 1;
                        if (use_background) support[shape.background] = 1;

                        std::vector<int> points;
                        for (int point = 0; point < n; ++point) {
                            if (support[point]) points.push_back(point);
                        }
                        if (static_cast<int>(points.size()) < k + 1) {
                            throw std::runtime_error("candidate-size drift");
                        }
                        std::vector<int> interpolation_points(
                            points.begin(), points.begin() + k
                        );
                        const auto polynomial = interpolate(
                            interpolation_points, xs, values, p
                        );
                        bool exact = true;
                        int agreement = 0;
                        for (int point = 0; point < n; ++point) {
                            bool agrees = eval(polynomial, xs[point], p) == values[point];
                            agreement += agrees;
                            if (agrees != static_cast<bool>(support[point])) {
                                exact = false;
                                break;
                            }
                        }
                        if (exact) {
                            ++retained;
                            ++agreement_histogram[agreement];
                            ++core_histogram[core_count];
                        }
                        if (processed % 100000 == 0) {
                            print_checkpoint(
                                n, mode, shard_index, shard_count,
                                processed, retained, began
                            );
                        }
                    }
                }
            }
        }
    }

    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - began
    ).count();
    std::cout << "L1_N10_RESULT {\"n\":" << n
              << ",\"k\":" << k
              << ",\"p\":" << p
              << ",\"mode\":\"" << mode
              << "\",\"shard_index\":" << shard_index
              << ",\"shard_count\":" << shard_count
              << ",\"global_candidates\":" << candidates
              << ",\"processed\":" << processed
              << ",\"retained\":" << retained
              << ",\"agreement_histogram\":{";
    bool first = true;
    for (const auto& [key, value] : agreement_histogram) {
        if (!first) std::cout << ",";
        std::cout << "\"" << key << "\":" << value;
        first = false;
    }
    std::cout << "},\"core_histogram\":{";
    first = true;
    for (const auto& [key, value] : core_histogram) {
        if (!first) std::cout << ",";
        std::cout << "\"" << key << "\":" << value;
        first = false;
    }
    std::cout << "},\"seconds\":" << seconds << "}" << std::endl;
    return retained;
}

int main(int argc, char** argv) {
    if (argc == 5) {
        const int n = std::stoi(argv[1]);
        const std::string mode = argv[2];
        const int shard_index = std::stoi(argv[3]);
        const int shard_count = std::stoi(argv[4]);
        if (n != 64 || (mode != "consec" && mode != "geom5") ||
            shard_count < 1 || shard_index < 0 || shard_index >= shard_count) {
            std::cerr << "invalid shard arguments" << std::endl;
            return 3;
        }
        census(n, 193, mode, shard_index, shard_count);
        return 0;
    }
    const auto known = census(16, 97, "consec");
    if (known != 43) {
        std::cerr << "L1_N10_REGRESSION_FAIL expected=43 actual=" << known << std::endl;
        return 2;
    }
    std::cout << "L1_N10_REGRESSION_PASS count=43" << std::endl;
    census(16, 97, "geom5");
    census(32, 97, "consec");
    census(32, 97, "geom5");
    return 0;
}
'''


@app.function(image=image, cpu=1, memory=1024, timeout=60, max_containers=64)
def run_census(payload: dict[str, object] | None = None) -> dict[str, object]:
    began = time.monotonic()
    with tempfile.TemporaryDirectory() as directory:
        source = f"{directory}/census.cpp"
        binary = f"{directory}/census"
        with open(source, "w", encoding="ascii") as handle:
            handle.write(CPP_SOURCE)
        compile_result = subprocess.run(
            ["g++", "-O3", "-std=c++17", source, "-o", binary],
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
        if compile_result.returncode:
            return {
                "app": APP_NAME,
                "complete": False,
                "stage": "compile",
                "returncode": compile_result.returncode,
                "stderr": compile_result.stderr[-4000:],
                "seconds": time.monotonic() - began,
            }
        command = [binary]
        if payload is not None:
            command.extend(
                [
                    str(payload["n"]),
                    str(payload["mode"]),
                    str(payload["shard_index"]),
                    str(payload["shard_count"]),
                ]
            )
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        lines: list[str] = []
        records: list[dict[str, object]] = []
        assert process.stdout is not None
        for line in process.stdout:
            line = line.rstrip("\n")
            lines.append(line)
            print(line, flush=True)
            if line.startswith("L1_N10_RESULT "):
                records.append(json.loads(line.removeprefix("L1_N10_RESULT ")))
        stderr = process.stderr.read() if process.stderr is not None else ""
        returncode = process.wait()
        return {
            "app": APP_NAME,
            "complete": returncode == 0,
            "returncode": returncode,
            "payload": payload,
            "lines": lines,
            "records": records,
            "stderr": stderr[-4000:],
            "seconds": time.monotonic() - began,
        }


@app.local_entrypoint()
def main(large: bool = False, shards: int = 32, retry: str = "") -> None:
    if not large:
        result = run_census.remote(None)
        print("L1_N10_MODAL_RESULT " + json.dumps(result, sort_keys=True))
        if not result["complete"]:
            raise SystemExit(1)
        return

    if not 1 <= shards <= 50:
        raise ValueError("shards must be in [1,50]")
    if retry:
        retry_shards = [int(item) for item in retry.split(",")]
        if any(item < 0 or item >= shards for item in retry_shards):
            raise ValueError("retry shard outside [0,shards)")
        tasks = [
            {
                "n": 64,
                "mode": "consec",
                "shard_index": shard,
                "shard_count": shards,
            }
            for shard in retry_shards
        ]
    else:
        tasks = [
            {"n": 64, "mode": mode, "shard_index": shard, "shard_count": shards}
            for mode in ("consec", "geom5")
            for shard in range(shards)
        ]
    results = list(run_census.map(tasks, return_exceptions=True))
    aggregates: dict[str, dict[str, object]] = {}
    failures: list[dict[str, object]] = []
    for task, result in zip(tasks, results):
        if isinstance(result, BaseException) or not result.get("complete"):
            failures.append({"task": task, "error": repr(result)})
            continue
        if len(result["records"]) != 1:
            failures.append({"task": task, "error": "result-record-count"})
            continue
        record = result["records"][0]
        mode = str(task["mode"])
        aggregate = aggregates.setdefault(
            mode,
            {
                "n": 64,
                "p": 193,
                "mode": mode,
                "shards": shards,
                "retained": 0,
                "processed": 0,
                "agreement_histogram": {},
                "core_histogram": {},
                "worker_seconds": 0.0,
            },
        )
        aggregate["retained"] += int(record["retained"])
        aggregate["processed"] += int(record["processed"])
        aggregate["worker_seconds"] += float(record["seconds"])
        for field in ("agreement_histogram", "core_histogram"):
            target = aggregate[field]
            for key, value in record[field].items():
                target[key] = target.get(key, 0) + int(value)
    expected_modes = 1 if retry else 2
    expected_processed = (
        sum((27152032 + shards - 1 - shard) // shards for shard in retry_shards)
        if retry
        else 27152032
    )
    complete = not failures and all(
        int(item["processed"]) == expected_processed for item in aggregates.values()
    ) and len(aggregates) == expected_modes
    summary = {
        "app": APP_NAME,
        "complete": complete,
        "tasks": len(tasks),
        "aggregates": aggregates,
        "failures": failures,
    }
    print("L1_N10_LARGE_RESULT " + json.dumps(summary, sort_keys=True))
    if not complete:
        raise SystemExit(1)
