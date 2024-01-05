# Below Step resolves "Paramiko", rust problem,

code is at this location:
C:\code\Work_MCM_ship_hats\new_pull_3\LoadValidate>

----------------------------------------------------------------------------------------------------
# -------------------How to create zip file-------------------------

https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-create-dependencies
Goto: To create the deployment package (project directory)  -- search this heading

pip install --no-cache-dir -r requirements.txt

pip install --no-cache-dir --target ./package -r requirements.txt  --- this wont work
this works:
pip3 install --platform manylinux2014_x86_64 --only-binary=:all: --target ./package -r requirements.txt
https://stackoverflow.com/questions/75389710/error-lib64-libc-so-6-version-glibc-2-28-not-found-required-by-var-task-c

For Quick ref: ubuntu
/mnt/c/code/Work_MCM_ship_hats/new_pull_3/LoadValidate

cd Package
zip -r ../LoadValidate.zip .

Run the below item post-code update
cd ..
zip LoadValidate.zip handler.py
zip LoadValidate.zip utility/ -r
zip LoadValidate.zip manifest_schema.json

---------------------------------------------------------------------------------------------------
# ------------------- To Deploy via CLI -------------------------

export AWS_PROFILE=MCM_SIT
set AWS_PROFILE=MCM_SIT

cd C:\code\Work_MCM_ship_hats\new_pull_3\LoadValidate>

aws lambda update-function-code --function-name "lmdb-bca-cnxmcm-sitezapp-loadvalidate" --zip-file fileb://LoadValidate.zip


-----------------------------------------------------------------------------------------------------


