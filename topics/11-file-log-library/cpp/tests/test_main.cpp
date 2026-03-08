#include "topic.hpp"
      #include <cassert>

      int main() {
        CliArgs args{};
args.input = "../fixtures/events.txt";
        assert(run(args) == "hello log\n");
        return 0;
      }
