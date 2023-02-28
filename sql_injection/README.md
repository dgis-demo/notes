## Get started
```bash
python3 main.py
./index.html
```

## Possible SQL injections
- `user1' or name='user2' or name='user3'--`
- `' or 1=1;--`
- `' union select password from users--`
- `' union select name || ':' || password from users--`
