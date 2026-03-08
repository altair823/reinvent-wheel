#include "topic.hpp"
#include <iostream>
#include <stdexcept>
#include <string>

namespace {
CliArgs parse_args(int argc, char** argv) {
  if (argc - 1 < 2 || argc - 1 > 2) {
    throw std::runtime_error("usage: t01_mini_grep_cpp <input> <query>");
  }
  CliArgs parsed{};
  parsed.input = argv[1];
  parsed.query = argv[2];
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
