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
Name   Value
test   test111
test2  test222
```

```
$ ssmp ls /test
Name       Value
/test/abc  test111
/test/cde  test
```

showing all columns

```
$ ssmp ls -a /
Name    Type    Value  Version LastModifiedDate
test   String  test111  1       19/12/12 21:09
test2  String  test222  1       19/12/16 20:31
```

list recursively

```
$ ssmp ls -r /
Name        Value
/test/abc   test111
/test/cde   test
test        test111
test2       test222
```

```
$ ssmp ls -ra /
Name        Type    Value    Version  LastModifiedDate
/test/abc   String  test111 1         19/12/12 21:11
/test/cde   String  test    1         19/12/16 20:32
test        String  test111 1         19/12/12 21:09
test2       String  test222 1         19/12/16 20:31
```

list without displaying header

```
$ ssmp ls -raq /
/test/abc   String  test111 1         19/12/12 21:11
/test/cde   String  test    1         19/12/16 20:32
test        String  test111 1         19/12/12 21:09
test2       String  test222 1         19/12/16 20:31
```

Search key under the path recursive or no recursive

```
$ ssmp grep ab /
Not found
```

```
$ ssmp grep -r ab /
Name       Value
/test/abc  test111
```

```
$ ssmp grep abc /test
Name       Value
/test/abc  test111
```

Search value of parameters

```
$ ssmp grep -rv 11 /
Name       Value
/test/abc  test111
test       test111
```

```
$ ssmp grep -v 11 /
Name       Value
test       test111
```

Run from docker to use local aws config

```
$ docker run --rm -v ~/.aws:/root/.aws yikaus/ssmp grep -rv 11 /
Name       Value
/test/abc  test111
test       test111
```
