rtq
======

Retrieve real time quotes fro yahoo finance

Install

    - git clone https://github.com/fja05680/rtq.git
    - cd rtq
    - sudo python setup.py install

Example

```python
import rtq
```


```python
symbols = 'SPY'
d = rtq.quote(symbols)
d
```




    {'SPY': 389.43}




```python
symbols = ['SPY', 'QQQ', 'TLT', 'GLD']
d = rtq.quote(symbols)
d
```




    {'SPY': 389.43, 'QQQ': 323.59, 'TLT': 141.06, 'GLD': 161.55}