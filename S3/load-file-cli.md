
1. Create bucket

```
aws s3 mb atifrani-bucket

aws s3 ls

aws s3 ls atifrani-bucket
```

3. Copy local file:

```
aws s3 cp file.txt s3://atifrani-bucket/data

aws s3 ls atifrani-bucket

aws s3 ls atifrani-bucket/data
```

3. romove file:

```
aws s3 rm  s3://atifrani-bucket/data/file.txt 

aws s3 ls atifrani-bucket/data
```

4. romove folder:

```
aws s3 rm  -r s3://atifrani-bucket/data --recursive

aws s3 ls atifrani-bucket
```

4. romove bucket:

````
aws s3 rb s3://atifrani-bucket/data --force

aws s3 ls atifrani-bucket
```