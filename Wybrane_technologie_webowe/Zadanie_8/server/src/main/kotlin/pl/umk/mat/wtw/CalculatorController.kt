package pl.umk.mat.wtw
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*

@CrossOrigin
@RestController
@RequestMapping("/")
class CalculatorController(
        private val calculatorService: CalculatorService
) {
    @PostMapping("")
    @ResponseStatus(HttpStatus.OK)
    fun calculate(
            @RequestBody input: Input
    ): Output {
        return calculatorService.calculate(input)
    }
}