# Zappa Vs SAM

## SAM does better

- Possibly better integrated with CodeDeploy (untested; since Zappa is also based around AWS it seems like it would also be basic to do)

## Zappa does better

- Async tasks easy to fire off to keep HTTP requests fast - runs in seperate lambda function

## Neutral

- When integrated with CodeDeploy both can gradually shift traffic to new Lambda function and rollback if alarms start to fire off

### Zappa

- Installed with pip (no homebrew required)

### SAM

- Tightly integrated with Docker