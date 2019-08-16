mkdir -p $VERSION
GIT_URL_N="$GIT_URL,$GIT_URL_1,$GIT_URL_2"
GIT_CIMMIT_N="$GIT_COMMIT,$GIT_COMMIT_1,$GIT_COMMIT_2"
echo "**********************************Start********************************"
#构建msmp-filling包
cd $WORKSPACE/msmp-filling && mvn clean package
mv msmp-filling-web/target/msmp-filling-web-dev-1.0-SNAPSHOT.war ../$VERSION/msmp-filling.war
#项目基线
git tag -a $VERSION -m $CHANGE_CONTENT
git push origin --tags
#构建msmp-filling-web包
cd $WORKSPACE/msmp-filling-web && cnpm install && npm run build
mv msmp-filling-web ../$VERSION
#项目基线
git tag -a $VERSION -m $CHANGE_CONTENT
git push origin --tags

#构建msmp-fmgr-web包
cd $WORKSPACE/msmp-fmgr-web && cnpm install && npm run build
mv msmp-fmgr-web ../$VERSION
#项目基线
git tag -a $VERSION -m $CHANGE_CONTENT
git push origin --tags

#归档SVN
svn import $WORKSPACE/$VERSION $SVN_ARCHIVE/$VERSION --username jenkins --password $jenkins -m "$VERSION" --force-log --no-auth-cache

#记录发布信息
cd $JENKINS_HOME/workspace && python ./rvl.py $ZENTAO_TEST_ID $JOB_NAME $VERSION $CHANGE_CONTENT $BUILD_TIMESTAMP $GIT_URL_N $GIT_CIMMIT_N $BUILD_TIMESTAMP $SVN_ARCHIVE/$VERSION $BUILD_USER $PUBLISHER $REMARKS

echo "**********************************End********************************"