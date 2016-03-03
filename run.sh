#!/bin/sh

cd source
tar zcf /usr/src/packages/SOURCES/hitvsupport.tar.gz *
cd -
rpmbuild -bb hitvsupport.spec --define="_topdir /usr/src/packages" 
#rpmbuild -bb hitvhap.spec --define="_hitvversion 5.2.0" --define="_hitvrelease 0" --define="_topdir /usr/src/packages"
