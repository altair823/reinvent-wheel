#include "topic.hpp"
      #include <cassert>

      int main() {
        CliArgs args{};
args.input = "../fixtures/expressions.txt";
        assert(run(args) == "hello expr\n");
        return 0;
      }
