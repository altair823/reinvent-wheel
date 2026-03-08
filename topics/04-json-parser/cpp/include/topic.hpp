#pragma once
#include <string>

struct CliArgs {
  std::string input;
};

std::string run(const CliArgs& args);
