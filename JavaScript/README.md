# Promises in JavaScript

## What is a Promise?
The promise object that represents the eventual completion (or failure) of an asynchronous operation, and its resulting value.

It can be in one of the three states:
- Pending: initial state, neither fulfilled nor rejected.
- Fulfilled: meaning that the operation completed successfully.
- Rejected: meaning that the operation failed.

Note: A promise is said to be settled when it is either fulfilled or rejected, but not pending.

## How to use a Promise?
For implementing promises. let's first look at it's skeleton, especially the input it takes and the methods it exposes.

It has a constructor function that takes a callback, and methods like then, catch and finally.

```javascript
const promise = new Promise((resolve, reject) => {
    /*
    your code logic goes here and you call resolve or reject(value)
    or reject(erroer) to resolve or reject the promise.
    */
})

promise.then((value) => {
    // code logic on success of an operation

}).catch((error) => {
    // code logic on failure of an operation

}).finally(() => {
    // code logic that will be executed regardless of the promise state
})
```

## _resolve() and reject() method implementation
```_resolve```` or ```_reject()``` set the ```state``` of promise to ```fulfilled``` or ```rejected``` respectively. They also set the ```value``` of the promise to the value passed to them.

NB: ```_resolve()``` and ```_reject()``` are not exposed to the user. They are used internally by the promise constructor.

Nothing happens if we try to call _resolve() or reject() on an already settled Promise

```

  _resolve = (value) => {
    this.updateResult(value, STATE.FULFILLED);
  }
  
  _reject = (error) => {
    this.updateResult(error, STATE.REJECTED);
  }
  
  updateResult(value, state) {
    // This is to make the processing async
    setTimeout(() => {
      /*
        Process the promise if it is still in pending state. 
        An already rejected or resolved promise is not processed
      */
      if (this.state !== STATE.PENDING) {
        return;
      }
    
      // check is value is also a promise
      if (isThenable(value)) {
        return value.then(this._resolve, this._reject);
      }
      
      this.value = value;
      this.state = state;
      
      // execute handlers if already attached
      this.executeHandlers();
    }, 0);
  }
```

Wondering what is ```isThenable()```? 
It is a function that checks if the value passed to ```_resolve()``` or ```_reject()``` is a promise or not. If it is a promise, it returns true, else false.

## isThenable() function implementation
A ```isThenable``` function checks if value is an instance of ```MyPromise``` or it is an object containing a ```then``` Function.

```
function isThenable(val) {
    return val instanceof MyPromise || 

}

// or 

function isThenable(value) {
    if (typeof value === "object" && value !== null) {
        if (typeof value.then === "function") {
            return true;
        }
        return false;
    }
}
```

## then() method implementation
```then()``` method takes two arguments, ```onFulfilled``` and ```onRejected```. Both are optional. If they are not a function, they are ignored.

```then()``` method returns a new promise. It takes care of the following scenarios:

then method takes two arguments as callbacks onSuccess and onFail.
onSuccess is called if Promise was fulfufilled and onFail is called if Promise was rejected.
then method returns a new Promise.

N/B: Remember that Promises can be chained
The essence of Promise chaining is that the ```then()``` method returns a new Promise object. That is how promises can be chained. This is specially useful in scenarios where we need to execute two or more asynchronous operations back to back.

Callbacks passed to ```then ()``` are stored in handlers array using ```addHandlers``` function. A handler function. A hanlder is an object { onSuccess, onFail} which will be executed when a promise is settled.



## catch() method implementation

```catch()``` is implemented using then(). We call ```then()``` method with ```onSuccess``` as ```null``` and pass ```onFail```  callback as second argument.

