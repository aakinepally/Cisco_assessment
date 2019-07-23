## Remember
Create a file called `settings.yaml` in same directory.
```
apikey:
  maddr: KEY
```

## Usage
Create a docker image.
```
sudo docker build -t image_name .
```

Now, run docker image
```
sudo docker run image_name:latest 44:38:39:ff:ef:57
```

This will print company name