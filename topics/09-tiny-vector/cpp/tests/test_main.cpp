#include "topic.hpp"
      #include <cassert>

      int main() {
        CliArgs args{};
args.input = "../fixtures/values.txt";
        assert(run(args) == "hello vector\n");
        return 0;
      }
