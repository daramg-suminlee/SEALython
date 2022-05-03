include(CPM)

CPMAddPackage(
  GITHUB_REPOSITORY pybind/pybind11
  VERSION 2.9.1
  )

cpmaddpackage(
  GITHUB_REPOSITORY microsoft/seal
  VERSION 4.0.0
  OPTIONS
  "SEAL_USE_MSGSL OFF"
  "SEAL_USE_ZLIB OFF"
)