package pl.umk.mat.wtw
import org.springframework.stereotype.Service

@Service
class CalculatorService {
    fun calculate(dto: Input): Output {
        return Output(
                if (dto.operator == Operator.ADD)
                    dto.first + dto.second
                else if (dto.operator == Operator.SUB)
                    dto.first - dto.second
                else if (dto.operator == Operator.MULTI)
                    dto.first * dto.second
                else if (dto.operator == Operator.DIV)
                    dto.first / dto.second
                else
                    0f

        )
    }
}