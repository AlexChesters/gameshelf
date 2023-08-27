set -e

REPOSITORY_NAME=$1

if [ -z $1 ]; then
  echo "[ERROR] - invalid usage"
  echo "example usage: sh ci/scripts/clean-ecr-image.sh my-ecr-repository-name"
  exit 1
fi

IMAGES=$(aws ecr-public describe-images \
  --repository-name $REPOSITORY_NAME \
  --region us-east-1 | jq -r .imageDetails)

UNTAGGED_IMAGES=$(jq -r 'map(select(has("imageTags") | not))' <<< $IMAGES)

IMAGE_DIGESTS=$(jq -r '[.[] | "imageDigest=\(.imageDigest)"] | join(" ")' <<< $UNTAGGED_IMAGES)

aws ecr-public batch-delete-image \
  --repository-name $REPOSITORY_NAME \
  --image-ids $IMAGE_DIGESTS \
  --region us-east-1
