# ONTDash (BETA)
Custom UI to manage Nokia ONT
- Currently tested on `G-2425G-A` but should work on other models too.
# UI
![image](https://user-images.githubusercontent.com/67057319/224267215-874a2be8-802a-4992-ab8b-86fe3d8ff08f.png)

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
