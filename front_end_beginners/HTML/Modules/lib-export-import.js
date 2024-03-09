let add=(n1, n2) => (n1+n2);
let multiply=(n1, n2)=>(n1*n2);
let math={
    add:add,
    multiply:multiply,
};

export default math;
export {add, multiply};

/*
//預設的輸出
let x="hello";
//export default x;
//非預設的輸出
let data=[5, 6, 7];
let obj={x:3, y:4, z:5};
//export{data, obj};

//整合輸出
export {x as default, data, obj};
*/