<?php
declare(strict_types=1);

namespace {{namespace}}\{{module_name}}\Cron;

use Psr\Log\LoggerInterface;

class TestCron
{

    /**
     * Constructor
     *
     * @param LoggerInterface $logger
     */
    public function __construct(private LoggerInterface $logger)
    {
        
    }

    /**
     * Execute the cron
     *
     * @return void
     */
    public function execute(): void
    {
        $this->logger->info("Cronjob TestCron is executed.");
    }
}