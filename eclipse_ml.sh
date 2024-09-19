#!/usr/bin/env bash
set -eu

# This is a bash script that is derived from the Eclipse's run script

java \
-Dfile.encoding=UTF-8 \
-classpath /Users/home/github_projects/ml/target/test-classes:/Users/home/github_projects/ml/target/classes:/Users/home/.m2/repository/com/jsbase/java-core/3.0/java-core-3.0.jar:/Users/home/.m2/repository/com/jsbase/java-testutil/3.0/java-testutil-3.0.jar:/Users/home/.m2/repository/junit/junit/4.13.2/junit-4.13.2.jar:/Users/home/.m2/repository/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar:/Users/home/.m2/repository/com/jsbase/java-graphics/3.0/java-graphics-3.0.jar:/Users/home/.m2/repository/commons-io/commons-io/2.6/commons-io-2.6.jar ml.Main --exceptions "$@"
