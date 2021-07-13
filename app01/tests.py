from django.test import TestCase

# Create your tests here.

json = {
    "apiVersion": "extensions/v1beta1",
    "kind": "Deployment",
    "metadata": {
        "name": "nginx",
        "labels": {
            "app": "nginx"
        }
    },
    "spec": {
        "replicas": 2,
        "selector": {
            "matchLabels": {
                "app": "nginx"
            }
        },
        "template": {
            "metadata": {
                "name": "nginx",
                "labels": {
                    "app": "nginx"
                }
            },
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "ntp.wei.club/nginx/nginx:latest",
                        "ports": [
                            {
                                "containerPort": 80
                            }
                        ],
                        "volumeMounts": [
                            {
                                "mountPath": "/usr/share/nginx/html",
                                "subPath": "nginx",
                                "name": "storage"
                            }
                        ]
                    }
                ],
                "volumes": [
                    {
                        "name": "storage",
                        "persistentVolumeClaim": {
                            "claimName": "nginx"
                        }
                    }
                ]
            }
        }
    }
}
import yaml,json
test_file = open("test_json_file","r")
test_json = json.loads(test_file)
test_dict = test_json
test_yaml = yaml.dump(test_dict)
#或者直接转换为文件
new_yaml_file = open("new_file","w")
yaml.safe_dump(test_dict,stream=new_yaml_file,default_flow_style=False)



