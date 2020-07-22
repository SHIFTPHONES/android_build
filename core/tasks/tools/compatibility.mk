# Copyright (C) 2015 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Package up a compatibility test suite in a zip file.
#
# Input variables:
#   test_suite_name: the name of this test suite eg. cts
#   test_suite_tradefed: the name of this test suite's tradefed wrapper
#   test_suite_dynamic_config: the path to this test suite's dynamic configuration file
#   test_suite_readme: the path to a README file for this test suite
#   test_suite_prebuilt_tools: the set of prebuilt tools to be included directly
#                         in the 'tools' subdirectory of the test suite.
#   test_suite_tools: the set of tools for this test suite
#
# Output variables:
#   compatibility_zip: the path to the output zip file.

out_dir := $(HOST_OUT)/$(test_suite_name)/android-$(test_suite_name)
test_artifacts := $(COMPATIBILITY.$(test_suite_name).FILES)
test_tools := $(HOST_OUT_JAVA_LIBRARIES)/hosttestlib.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/tradefed.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/tradefed-no-fwk.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/tradefed-test-framework.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/loganalysis.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/compatibility-host-util.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/compatibility-host-util-tests.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/compatibility-common-util-tests.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/compatibility-tradefed-tests.jar \
  $(HOST_OUT_JAVA_LIBRARIES)/$(test_suite_tradefed).jar \
  $(HOST_OUT_JAVA_LIBRARIES)/$(test_suite_tradefed)-tests.jar \
  $(HOST_OUT_EXECUTABLES)/$(test_suite_tradefed) \
  $(test_suite_readme)

test_tools += $(test_suite_tools)

# Include host shared libraries
host_shared_libs := $(call copy-many-files, $(COMPATIBILITY.$(test_suite_name).HOST_SHARED_LIBRARY.FILES))

compatibility_zip_deps := $(test_artifacts) $(test_tools) $(test_suite_prebuilt_tools) $(test_suite_dynamic_config) $(SOONG_ZIP) $(host_shared_libs)
compatibility_zip_resources := $(out_dir)/tools $(out_dir)/testcases
ifdef test_suite_notice
	compatibility_zip_deps += $(test_suite_notice)
	compatibility_zip_resources += $(out_dir)/$(notdir $(test_suite_notice))
endif

compatibility_zip := $(out_dir).zip
$(compatibility_zip): PRIVATE_NAME := android-$(test_suite_name)
$(compatibility_zip): PRIVATE_OUT_DIR := $(out_dir)
$(compatibility_zip): PRIVATE_TOOLS := $(test_tools) $(test_suite_prebuilt_tools)
$(compatibility_zip): PRIVATE_SUITE_NAME := $(test_suite_name)
$(compatibility_zip): PRIVATE_DYNAMIC_CONFIG := $(test_suite_dynamic_config)
$(compatibility_zip): PRIVATE_NOTICE := $(test_suite_notice)
$(compatibility_zip): PRIVATE_RESOURCES := $(compatibility_zip_resources)
$(compatibility_zip): $(compatibility_zip_deps) | $(ADB) $(ACP)
# Make dir structure
	$(hide) mkdir -p $(PRIVATE_OUT_DIR)/tools $(PRIVATE_OUT_DIR)/testcases
	$(hide) echo $(BUILD_NUMBER_FROM_FILE) > $(PRIVATE_OUT_DIR)/tools/version.txt
# Copy tools
	$(hide) cp $(PRIVATE_TOOLS) $(PRIVATE_OUT_DIR)/tools
	$(if $(PRIVATE_DYNAMIC_CONFIG),$(hide) cp $(PRIVATE_DYNAMIC_CONFIG) $(PRIVATE_OUT_DIR)/testcases/$(PRIVATE_SUITE_NAME).dynamic)
	$(if $(PRIVATE_NOTICE),$(hide) cp $(PRIVATE_NOTICE) $(PRIVATE_OUT_DIR))
	$(hide) find $(PRIVATE_RESOURCES) | sort >$@.list
	$(hide) $(SOONG_ZIP) -d -o $@ -C $(dir $@) -l $@.list

# Reset all input variables
test_suite_name :=
test_suite_tradefed :=
test_suite_dynamic_config :=
test_suite_readme :=
test_suite_prebuilt_tools :=
test_suite_tools :=
test_suite_notice :=
host_shared_libs :=
