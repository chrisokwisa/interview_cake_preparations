function deleteNode(nodeToDelete) {
    
    // Get the input node's next node, the one we want to skip
    const nextNode = nodeToDelete.next;

    if (nextNode) {

        // Replace the input node's value and pointer with next
        // node's value and pointer. The previous node now effectively
        // skips over the iput node

        nodeToDelete.value = nextNode.value;
        nodeToDelete.next = nextNode.next;
    } 
    else {
        // trying to delete the last node
        throw new Error("Can't delete the last node with technique!");
    }
}