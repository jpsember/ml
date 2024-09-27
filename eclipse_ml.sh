#!/usr/bin/env bash
set -eu

# This is a bash script that is derived from the Eclipse's run script

java \
-Dfile.encoding=UTF-8 \
-classpath /Users/home/github_projects/ml/target/classes:/Users/home/.m2/repository/com/jsbase/java-core/1000/java-core-1000.jar:/Users/home/.m2/repository/com/jsbase/java-graphics/3.1/java-graphics-3.1.jar:/Users/home/.m2/repository/commons-io/commons-io/2.6/commons-io-2.6.jar ml.Main --exceptions "$@"
