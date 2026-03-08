#include "topic.hpp"
      #include <cassert>

      int main() {
        CliArgs args{};
args.input = "../fixtures/sample.json";
        assert(run(args) == "hello json\n");
        return 0;
      }
