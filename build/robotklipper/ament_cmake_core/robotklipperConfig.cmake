# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_robotklipper_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED robotklipper_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(robotklipper_FOUND FALSE)
  elseif(NOT robotklipper_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(robotklipper_FOUND FALSE)
  endif()
  return()
endif()
set(_robotklipper_CONFIG_INCLUDED TRUE)

# output package information
if(NOT robotklipper_FIND_QUIETLY)
  message(STATUS "Found robotklipper: 0.0.0 (${robotklipper_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'robotklipper' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${robotklipper_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(robotklipper_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${robotklipper_DIR}/${_extra}")
endforeach()
