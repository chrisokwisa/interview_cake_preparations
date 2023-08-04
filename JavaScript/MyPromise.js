const STATE = {
    PENDING: 'PENDING',
    FULFILLED: 'FULFILLED',
    REJECTED: 'REJECTED',

}

function isThenable(value) {
    return value instanceof MyPromise;
}

class MyPromise {
    constructor(callback) {
        // Intial state of promise is empty
        this.state = STATE.PENDING;
        this.state = undefined
        this.handlers = [];
        // Invoke callback by passing the _resolve and the _reject function of our class
        try {
            callback(this._resolve, this._reject);

        } catch (err) {
            this._reject(err)
        }
    }

    _resolve = (value) => {
        this.updateResult(value, STATE.FULFILLED);

    }

    _reject = (error) => {
        this.updateResult(error, STATE.REJECTED);
    }

    updateResult(value, state) {
        setTimeout(() => {
        // process the promise if it is still in pending state
        
        if (this.state !== STATE.PENDING) {
            return
        }

        // check if value is also a promise
        if (isThenable(value)) {
            return value.then(this._resolve, this._reject);
        }

        this.value = value;
        this.state = state;

        // execute handlers if already attached
        this.executeHandlers();
    }, 0);
    }

    addHandlers(handlers) {
        this.handlers.push(handlers);
        this.executeHandlers();
    }

    executeHandlers() {
        // Don't execute handlers if promise is not yet fulfilled or rejected
        if (this.state === STATE.PENDING) {
            return null;
        }

        // we have multiple handlers because add them for .finally block too
        this.handlers.forEach((handler) => {
            if (this.state === STATE.FULFILLED) {
                return handler.onSuccess(this.value);
            }
            return handler.onFail(this.value);
        });
        // After processing all handlers, we reset it to empty.
        this.handlers = [];
        }

    then(onSuccess, onFail) {
        // return a new promise
       return new MyPromise((res, rej) => {
        this.addHandlers({
            onSuccess: function(value) {
                // if onSuccess is not a function, we just pass the value to the next promise
                if (!onSuccess) { // if onSuccess is not a function, we just pass the value to the next promise
                    return res(value);
                }

                try {
                    return res(onSuccess(value));

                } catch(error) { // if onSuccess throws an error, we reject the next promise
                    return rej(error); 
                }
            },

            onFail: function(value) {
                // if onFail provided, reject the value for the next promise
                if (!onFail) {
                    return reject(value);
                }

                try {
                    return resolve(onFail(value));

                } catch(error) {
                    return reject(error);
                }
            }
        });
       });
    }

    // Since then method take the second function as onFail, we can leverage it while implementing catch
    catch(onFail) {
        return this.then(null, onFail);
    }


    finally(callback) {
        return new MyPromise((res, rej) => {
           let val;
           let wasRejected;
           this.then((value) => {
             wasRejected = false;
             val = value;
             return callback();
           }, (err) => {
             wasRejected = true;
             val = err;
             return callback();
           }).then(() => {
             // If the callback didn't have any error we resolve/reject the promise based on promise state
             if(!wasRejected) {
               return res(val);
             } 
             return rej(val);
           })
        })
      }
    }

    // Tests

const testPromiseWithLateResolve = new MyPromise((resolve, reject) => {
    setTimeout(() => {
        resolve('Promise 1 is resolved');
    }, 1000);
});

testPromiseWithLateResolve.then((value) => {
    console.log('Resolved: ', value);
});

const testPromiseWithLateReject = new MyPromise((resolve, reject) => {
    setTimeout(() => {
        reject('Promise 2 is rejected');
    }, 1000);
});

testPromiseWithLateReject.then((value) => {
    console.log(value);
}).catch((err) => {
    console.log(err);
});


