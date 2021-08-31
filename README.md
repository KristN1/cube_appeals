# Cube Appeals 0.1.0

Python package for CubeCraft appeals page that allows you to get player's appeal link, check if he's banned or get their appeal status.

This package is not yet fully released as there are issues with the pip install but you can install it from [Test PyPi site](https://test.pypi.org/project/cube-appeals/)

```
$ pip install -i https://test.pypi.org/simple/ cube-appeals
```
```
$ pip install undetected-chromedriver
```

It is recommended to **use VPN** when running code with this package as you might get rate-limited.

### Example:
```py
from cube_appeals import check_appeal

print(check_appeal.java("KristN_"))
```

### To Do:
- [ ] Use chromedriver headless mode 
- [ ] Fix undetected-crhomedriver not installing with the package
- [ ] Add rate limit exception