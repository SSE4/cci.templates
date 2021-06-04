cmake_minimum_required(VERSION 3.1)
project(test_package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package({{ name }} REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.cpp)
# uncomment for C
# add_executable(${PROJECT_NAME} test_package.c)
target_link_libraries(${PROJECT_NAME} {{ name }}::{{ name }})
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 11)
