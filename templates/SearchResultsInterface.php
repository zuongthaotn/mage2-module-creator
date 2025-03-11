<?php
namespace {{namespace}}\{{module_name}}\Api\Data;

use Magento\Framework\Api\SearchResultsInterface;

/**
 * Interface for search results.
 * @api
 * @since 100.0.2
 */
interface {{interface_name}}SearchResultsInterface extends SearchResultsInterface
{
    /**
     * Get list.
     *
     * @return \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface[]
     */
    public function getItems();

    /**
     * Set list.
     *
     * @param \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface[] $items
     * @return $this
     */
    public function setItems(array $items);
}
