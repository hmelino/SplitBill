# SplitBill
> Split bill easily.

## Why use SplitBill ?
Imagine day when friends pay for different bills on day. One pays for drinks, another pay for whole meal and third one pay for karaoke booking. Add fact that not all friends were there for karaoke, or somebody had to leave early and didn't come for last drinks and splitting bill can become confusing.

That's where python script SplitBill comes. You can easily define categories and add separate payments from friends.
At the end you get clear amount for each friend to pay/receive. 
## Installation
### Clone

- Clone this repo to your local machine using ' git clone https://github.com/hmelino/SplitBill.git'

### Use

---


> Import the package 

```Python
from SplitBill import SBill
```

> Initialise new object with SBill module and add activities/meals/thingsToBePaidFor as an arguments.

```Python
lastSaturday=SBill('prosseco','karaoke','karaoke2')
```
> Add all guests starting with their name first and then activities in same order as when created object above.
* use 0 if person attended given event, but didn't pay anything yet
* use None is person didn't attend given event 
* use any positive number if person paid for something on this event
```Python
lastSaturday.addPerson('Mike',0,0,30)
lastSaturday.addPerson('Suzi',80,0,20)
lastSaturday.addPerson('Jacob',None,0,0)
lastSaturday.addPerson('Elena',0,0,0)
```
> Calculate results
```Python
lastSaturday.calculateBill()
```

> Result will be :
```shell
Mike should pay £9.17
Suzi will recieve £60.83
Jacob should pay £12.5
Elena should pay £39.17
```
> In this case Suzi will receive £60.83 which is sum of all payments.
---

## Contact

- Website at <a href="https://github.com/hmelino" target="_blank">`https://github.com/hmelino`</a>


