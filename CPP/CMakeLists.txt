cmake_minimum_required(VERSION 3.17)
project(CPP)

set(CMAKE_CXX_STANDARD 20)

add_executable(CPP main.cpp module/Vector.hpp module/Point.cpp module/Point.hpp module/SetCircle.cpp module/SetCircle.hpp module/Line.cpp module/Line.hpp svg.hpp module/setLine.cpp module/setLine.hpp module/base.cpp module/base.hpp module/file_operation.cpp module/file_operation.h)