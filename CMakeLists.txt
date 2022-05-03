cmake_minimum_required(VERSION 3.19)
project(SEALython)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Python3 COMPONENTS Interpreter Development)

add_library(seal_pybind MODULE src/wrapper.cpp)

target_include_directories(seal_pybind
  PUBLIC
    ${pybind11_SOURCE_DIR}/include
    ${seal_SOURCE_DIR}/native/src
    ${Python3_INCLUDE_DIRS}
  )

target_link_libraries(seal_pybind
  PUBLIC
    pybind11::module
    seal
  )

target_link_libraries(seal_pybind PUBLIC)

add_subdirectory(external)

set_target_properties(seal_pybind
  PROPERTIES OUTPUT_NAME "seal"
  PREFIX "${PYTHON_MODULE_PREFIX}"
  SUFFIX "${PYTHON_MODULE_EXTENSION}")

install(
  TARGETS seal_pybind
  LIBRARY DESTINATION lib
  )