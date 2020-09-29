# sitepipes

The sitepipes framework performs computations across datasets that may or not be on the same host machine. It revolves around the idea of a site: a host machine (or cluster) that has access to one or more datasets and/or models.

The framework is designed to be similar to the plumbing in a home. There are "pipes" to move data from Point A to Point B (like water pipes). There are "tanks" for cached data (like water tanks). There are "fittings" to connect two or more pipes (like pipe fittings). And so much more!

It uses PySyft, which is a wrapper for Torch tensor operations with additional federated learning operations. 

It contains web components for web frameworks like React and Angular.
