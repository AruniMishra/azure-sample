package com.function;

import com.microsoft.azure.functions.ExecutionContext;
import com.microsoft.azure.functions.annotation.FunctionName;
import com.microsoft.azure.functions.annotation.ServiceBusQueueTrigger;

/**
 * Azure Functions with ServiceBusQueue Trigger.
 */
public class Function {
 
    @FunctionName("sbprocessor")
    public void serviceBusProcess(
    @ServiceBusQueueTrigger(name = "msg",
                             queueName = "javaqueue",
                             connection = "myconnvarname") String message,
   final ExecutionContext context
 ) {
     context.getLogger().info(message);
 }
}
