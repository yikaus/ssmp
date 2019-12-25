# AWS SSM parameter helper cli I created for myself

### Install

`pip3 install ssmp`

### Usage

`ssmp --help`

use docker

`docker run yikaus/ssmp`

### Example

list all parameters only under the path , no recursive.

```
$ ssmp ls /
Name    Type    Value  Version LastModifiedDate
test  String  test111        1   19/12/12 21:09
test2  String  test222        1   19/12/16 20:31
$ ssmp ls /test
Name    Type    Value  Version LastModifiedDate
/test/abc  String  test111        1   19/12/12 21:11
/test/cde  String     test        1   19/12/16 20:32
```

Search key under the path recursive or no recursive

```
$ ssmp grep ab /
Not found
$ ssmp grep -r ab /
Name    Type    Value  Version LastModifiedDate
/test/abc  String  test111        1   19/12/12 21:11
$ ssmp grep abc /test
Name    Type    Value  Version LastModifiedDate
/test/abc  String  test111        1   19/12/12 21:11
```

Search key on value of parameters

```
$ ssmp grep -rv 11 /
Name    Type    Value  Version LastModifiedDate
/test/abc  String  test111        1   19/12/12 21:11
test  String  test111        1   19/12/12 21:09
$ ssmp grep -v 11 /
Name    Type    Value  Version LastModifiedDate
test  String  test111        1   19/12/12 21:09
```

Run from docker to use local aws config

```
$ docker run --rm -v ~/.aws:/root/.aws yikaus/ssmp grep -rv 11 /
Name    Type    Value  Version LastModifiedDate
/test/abc  String  test111        1   19/12/12 10:11
test  String  test111        1   19/12/12 10:09
```
