#include "topic.hpp"
      #include <cassert>

      int main() {
        CliArgs args{};
args.input = "../fixtures/sample.txt";
args.query = "Rust";
        assert(run(args) == "hello grep\n");
        return 0;
      }
