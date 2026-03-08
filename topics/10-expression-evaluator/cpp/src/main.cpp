#include "topic.hpp"
#include <iostream>
#include <stdexcept>
#include <string>

namespace {
CliArgs parse_args(int argc, char** argv) {
  if (argc - 1 < 1 || argc - 1 > 1) {
    throw std::runtime_error("usage: t10_expression_evaluator_cpp <input>");
  }
  CliArgs parsed{};
  parsed.input = argv[1];
  return parsed;
}
}

int main(int argc, char** argv) {
  try {
    auto args = parse_args(argc, argv);
    std::cout << run(args);
    return 0;
  } catch (const std::exception& ex) {
    std::cerr << ex.what() << "\n";
    return 1;
  }
}
