# get script directory
$ScriptPath = $MyInvocation.MyCommand.Path
$ScriptDir = Split-Path $ScriptPath
cd $ScriptDir
kubectl delete -f .\example.yaml
cd backend
docker build -t backend .
cd ../frontend
docker build -t frontend .
cd ..
kubectl apply -f .\example.yaml