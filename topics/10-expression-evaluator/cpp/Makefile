CXX ?= g++
CXXFLAGS ?= -std=c++23 -O2 -Wall -Wextra -pedantic -Iinclude
BIN_DIR := bin
APP := $(BIN_DIR)/t10_expression_evaluator_cpp
TEST_BIN := $(BIN_DIR)/t10_expression_evaluator_cpp_tests
.PHONY: build run test e2e smoke clean

$(APP): src/main.cpp src/lib.cpp include/topic.hpp
	mkdir -p $(BIN_DIR)
	$(CXX) $(CXXFLAGS) src/main.cpp src/lib.cpp -o $(APP)

$(TEST_BIN): tests/test_main.cpp src/lib.cpp include/topic.hpp
	mkdir -p $(BIN_DIR)
	$(CXX) $(CXXFLAGS) tests/test_main.cpp src/lib.cpp -o $(TEST_BIN)

build: $(APP) $(TEST_BIN)

run: $(APP)
	./$(APP) ../fixtures/expressions.txt

test: $(TEST_BIN)
	./$(TEST_BIN)

e2e:
	bash ../e2e/cpp-smoke.sh

smoke: run

clean:
	rm -rf $(BIN_DIR)
