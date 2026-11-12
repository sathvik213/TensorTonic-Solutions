def value_addition_node(left: dict, right: dict, output_id: str) -> dict:
    """
    Returns an addition node with id, data, grad, op, and the original parents.
    """
    # pass

    output_node={
                "id":"",
                "data":0,
                "grad":0.0,
                "op":"+",
                "parents":[]
    }

    output_node['data']=float(left['data'])+float(right['data'])
    output_node['id']=output_id
    output_node['parents']= [left,right]
    return output_node
    
