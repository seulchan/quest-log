// Rewrite the factorial function using a `while` loop.
pub fn factorial(n: u32) -> u32 {
    // The `todo!()` macro is a placeholder that the compiler
    // interprets as "I'll get back to this later", thus
    // suppressing type errors.
    // It panics at runtime.
    let mut sum = 1;
    let mut i = n;
    while i > 0 {
        sum = sum * i;
        i = i - 1;
    }
    sum
}
