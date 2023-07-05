# Learning React.Js from scratch

## What is React.Js?
React is a JavaScript library for building user interfaces. It is maintained by Facebook and a community of individual developers and companies. React can be used as a base in the development of single-page or mobile applications.

## Why React.Js?
React allows developers to create large web applications that can change data, without reloading the page. The main purpose of React is to be fast, scalable, and simple. It works only on user interfaces in the application. This corresponds to the view in the MVC template. It can be used with a combination of other JavaScript libraries or frameworks, such as Angular JS in MVC.

## What is JSX?
JSX stands for JavaScript XML. JSX allows us to write HTML in React. JSX makes it easier to write and add HTML in React.

## What is Virtual DOM?
The virtual DOM (VDOM) is an in-memory representation of Real DOM. The representation of a UI is kept in memory and synced with the "real" DOM. It's a step that happens between the render function being called and the displaying of elements on the screen. This entire process is called reconciliation.   

## What is the difference between Real DOM and Virtual DOM?
| Real DOM | Virtual DOM |
| --- | --- |
| It updates slow | It updates faster |
| Can directly update HTML | Can't directly update HTML |
| Creates a new DOM if element updates | Updates the JSX if element updates |
| DOM manipulation is very expensive | DOM manipulation is very easy |
| Too much of memory wastage | No memory wastage |

## What is the difference between state and props?
| State | Props |
| --- | --- |
| State is mutable | Props are immutable |
| State is local | Props can be accessed by child components |
| State affects only the component where it is declared | Props can affect multiple components, but only in one direction |

## What is the purpose of callback function as an argument of setState()?
The callback function is invoked when setState finished and the component gets rendered. Since setState() is asynchronous the callback function is used for any post action.

## What is the difference between HTML and React event handling?
| HTML | React |
| --- | --- |
| HTML events are named in lowercase | React events are named in camelCase |
| HTML event handlers return false to prevent default browser behaviour | React event handlers must call preventDefault() explicitly |

## What are synthetic events in React?
Synthetic events are the objects which act as a cross-browser wrapper around the browser's native event. They combine the behavior of different browsers into one API. This is done to make sure that the events show consistent properties across different browsers.

## What is the difference between createElement and cloneElement?
createElement() is used to create a new element while cloneElement() is used to clone an element and then edit it by passing the parameter props.

## What is the difference between stateless and stateful components?
| Stateless | Stateful |
| --- | --- |
| Stateless components are functional components | Stateful components are class components |
| Stateless components do not have access to lifecycle methods | Stateful components can have access to lifecycle methods |
| Stateless components can update props | Stateful components can update state |

## What are Higher-Order components?
Higher-Order components are the components that take other components as an argument and return a new component.

## What is context?
Context provides a way to pass data through the component tree without having to pass props down manually at every level.

## What is the purpose of using super constructor with props argument?
A child class constructor cannot make use of this reference until super() method has been called. The same applies for ES6 sub-classes as well. The main reason of passing props parameter to super() call is to access this.props in your child constructors.

## What is reconciliation?
When a component's props or state change, React decides whether an actual DOM update is necessary by comparing the newly returned element with the previously rendered one. When they are not equal, React will update the DOM. This process is called reconciliation.

## What is the difference between Element and Component?
An Element is a plain object describing what you want to appear on the screen in terms of the DOM nodes or other components. Elements can contain other Elements in their props. Creating a React element is cheap. Once an element is created, it is never mutated.

A component can be declared in several different ways. It can be a class with a render() method. Alternatively, in simple cases, it can be defined as a function. In either case, it takes props as an input, and returns an element tree as the output. The main advantage of defining components as classes is that they can have some local state. Note that defining a component as a function is typically a lot simpler.

## What are Pure Components?
React.PureComponent is exactly the same as React.Component except that it handles the shouldComponentUpdate() method for you. When props or state changes, PureComponent will do a shallow comparison on both props and state. Component on the other hand won't compare current props and state to next out of the box. Thus, the component will re-render by default whenever shouldComponentUpdate is called.

## What is the purpose of using super(props)?
A child class constructor cannot make use of this reference until super() method has been called. The same applies for ES6 sub-classes as well. The main reason of passing props parameter to super() call is to access this.props in your child constructors.

## What is the difference between constructor and getInitialState?
constructor is used to initialize local state of a component whereas getInitialState is used to initialize the state of a component which will be initialized only once.

## What is the difference between state and props?
| State | Props |
| --- | --- |
| State is mutable | Props are immutable |


## What is the difference between createElement and cloneElement?
createElement() is used to create a new element while cloneElement() is used to clone an element and then edit it by passing the parameter props.

## What is the difference between stateless and stateful components?
| Stateless | Stateful |
| --- | --- |
| Stateless components are functional components | Stateful components are class components |
| Stateless components do not have access to lifecycle methods | Stateful components can have access to lifecycle methods |

## What are Higher-Order components?
Higher-Order components are the components that take other components as an argument and return a new component.

## What is context?
Context provides a way to pass data through the component tree without having to pass props down manually at every level.

## What is the purpose of using super constructor with props argument?
A child class constructor cannot make use of this reference until super() method has been called. The same applies for ES6 sub-classes as well. The main reason of passing props parameter to super() call is to access this.props in your child constructors.

## What is reconciliation?
When a component's props or state change, React decides whether an actual DOM update is necessary by comparing the newly returned element with the previously rendered one. When they are not equal, React will update the DOM. This process is called reconciliation.

## What is the difference between Element and Component?
An Element is a plain object describing what you want to appear on the screen in terms of the DOM nodes or other components. Elements can contain other Elements in their props. Creating a React element is cheap. Once an element is created, it is never mutated.

