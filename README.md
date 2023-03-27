# ONTDash (BETA)
Custom UI to manage Nokia ONT
- Currently tested on `G-2425G-A` but should work on other models too.
# UI
![image](https://user-images.githubusercontent.com/67057319/227887010-0a47de5f-11c2-429f-9040-8e328837826e.png)

# Dependencies 
`python3`
`sshpass`
`flask` 

## How to run

Currently ONTDash is in beta stage, I will make a easy to install docker image once it's in a "good enough" state.

```sh
git clone https://github.com/Albonycal/ONTDash
```


```sh 
cd ONTDash
```

You need to setup the environment variable `ONTPASS` as your ONT's password,
add that to your shell's rc file (ex `.bashrc` )


```sh
export ONTPASS=<Password>
```


```sh
python app.py&

```
