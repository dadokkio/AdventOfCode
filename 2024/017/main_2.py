class Machine:
    def __init__(self, register_a, register_b, register_c, program):
        self.registers = {"A": register_a, "B": register_b, "C": register_c}
        self.program = program
        self.instruction_pointer = 0
        self.output_values = []

        self.instructions = {
            0: self._div_register("A"),
            1: lambda operand: self._bitwise_xor_literal(operand),
            2: lambda operand: self._set_register("B", operand),
            3: self._jump_if_nonzero,
            4: self._bitwise_xor_registers,
            5: self._output,
            6: self._div_register("B"),
            7: self._div_register("C"),
        }

    def _div_register(self, register):
        def div(operand):
            denominator = 2 ** self._get_operand_value(operand)
            self.registers[register] = self.registers["A"] // denominator
            self.increment_pointer()

        return div

    def _bitwise_xor_literal(self, operand):
        self.registers["B"] ^= operand
        self.increment_pointer()

    def _set_register(self, register, operand):
        self.registers[register] = self._get_operand_value(operand) % 8
        self.increment_pointer()

    def _jump_if_nonzero(self, operand):
        if self.registers["A"] != 0:
            self.instruction_pointer = operand
        else:
            self.increment_pointer()

    def _bitwise_xor_registers(self, operand):
        self.registers["B"] ^= self.registers["C"]
        self.increment_pointer()

    def _output(self, operand):
        self.output_values.append(self._get_operand_value(operand) % 8)
        self.increment_pointer()

    def _get_operand_value(self, operand):
        operand_map = {0: 0, 1: 1, 2: 2, 3: 3, 4: "A", 5: "B", 6: "C"}
        return self.registers[operand_map[operand]] if operand > 3 else operand

    def increment_pointer(self):
        self.instruction_pointer += 2

    def run_instruction(self, opcode, operand):
        self.instructions[opcode](operand)

    def run_program(self):
        while self.instruction_pointer < len(self.program) - 1:
            opcode, operand = self.program[
                self.instruction_pointer : self.instruction_pointer + 2
            ]
            self.run_instruction(opcode, operand)

    def check_output(self):
        if not self.output_values:
            return

        for i in range(len(self.output_values)):
            if self.output_values[i] != self.program[i]:
                self.instruction_pointer = float("inf")
                break


if __name__ == "__main__":
    with open(file="input.txt", mode="r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        register_b = int(lines[1][12:])
        register_c = int(lines[2][12:])
        program = list(map(int, lines[4][9:].split(",")))

    valid = [0]
    for length in range(1, len(program) + 1):
        oldValid = valid.copy()
        valid = []
        for num in oldValid:
            for offset in range(8):
                newNum = 8 * num + offset
                machine = Machine(
                    register_a=newNum,
                    register_b=register_b,
                    register_c=register_c,
                    program=program,
                )
                machine.run_program()
                output = machine.output_values
                if output[-length:] == program[-length:]:
                    valid.append(newNum)
    print(min(valid))
