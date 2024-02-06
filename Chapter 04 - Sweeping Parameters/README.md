Incremental development is a way of programming that tries to minimize the pain of debugging. 

The fundamental steps are:
1. Always start with a working program. If you have an example from a book, or a program you wrote that is similar to what you are working on, start with that. Otherwise, start with something you know is correct,
like x=5. Run the program and con rm that it does what you expect.
2. Make one small, testable change at a time. A testable change is one that displays something or has some other effect you can check. Ideally, you should know what the correct answer is, or be able to check it by
performing another computation.
3. Run the program and see if the change worked. If so, go back to Step 2. If not, you will have to do some debugging, but if the change you made was small, it shouldnt take long to find the problem.

When this process works, your changes usually work the rst time, or if they dont, the problem is obvious. In practice, there are two problems with incremental development:
- Sometimes you have to write extra code to generate visible output that you can check. This extra code is called sca olding because you use it to build the program and then remove it when you are done. That might seem like a waste, but time you spend on scaffolding is almost always time you save on debugging.
- When you are getting started, it might not be obvious how to choose the steps that get from x=5 to the program you are trying to write. You will see more examples of this process as we go along, and you will get better with experience.