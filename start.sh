# get script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
kubectl delete -f ./example.yaml
cd backend
docker build -t backend .
cd ../frontend
docker build -t frontend .
cd ..
kubectl apply -f ./example.yaml