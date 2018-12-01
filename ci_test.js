const $ = require('shelljs')
const path = require('path')

const root = path.join(__dirname)

try {
    console.info('Running python test module: pytest')
    $.cd(root)
    let pytest_results = $.exec(`pytest`).code
    /**
     * From pytest documentation:
     * https://docs.pytest.org/en/latest/usage.html#possible-exit-codes
     *
     * Running pytest can result in six different exit codes:
     * Exit code 0:	All tests were collected and passed successfully
     * Exit code 1:	Tests were collected and run but some of the tests failed
     * Exit code 2:	Test execution was interrupted by the user
     * Exit code 3:	Internal error happened while executing tests
     * Exit code 4:	pytest command line usage error
     * Exit code 5:	No tests were collected
     */
    switch (pytest_results) {
        case 0:
            console.info('Pytest => All tests were collected and passed successfully')
            break;
        case 1:
            console.error('Pytest => Tests were collected and run but some of the tests failed')
            process.exit(1)
            break;
        case 2:
            console.error('Pytest => Test execution was interrupted by the user')
            process.exit(2)
            break;
        case 3:
            console.error('Pytest => Internal error happened while executing tests')
            process.exit(3)
            break;
        case 4:
            console.error('Pytest => pytest command line usage error')
            process.exit(4)
            break;
        case 5:
            console.error('Pytest => No tests were collected')
            process.exit(5)
            break;
    }
} catch (error) {
    console.error(error)
    process.exit(1)
}

console.info(`✅ Build succeeded`)